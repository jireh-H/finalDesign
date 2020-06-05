// pages/goods_detail/goods_detail.js
import { request } from "../../service/network.js"

Page({

  /**
   * 页面的初始数据
   */
  data: {
    goodsObj: {},
  },

  //商品对象
  GoodsInfo: {},

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    let pages = getCurrentPages();
    let currentPage = pages[pages.length - 1];
    let options = currentPage.options;
    const { id } = options;
    this.getGoodsDetail(id);
  },

  //获取商品详情数据
  getGoodsDetail(id) {
    request({ url: 'foodInfo', data: { id } })
      .then(res => {
        console.log(res)
        this.GoodsInfo = res.data.message;
        //1 获取缓存中的商品收藏的数组
        this.setData({
          goodsObj: res.data.message,
        })
      })
  },

  //点击 加入购物车
  handleCartAdd() {
    //1 获取缓存中的购物车数组
    let cart = wx.getStorageSync('cart') || [];
    //2 判断 商品对象是否存在于购物车数组中
    let index = cart.findIndex(v => v.id === this.GoodsInfo.id);
    if (index === -1) {
      //3 不存在 第一次添加
      this.GoodsInfo.num = 1;
      //选中状态
      this.GoodsInfo.checked = true;
      cart.push(this.GoodsInfo);
    } else {
      //已经存在购物车数据 执行num++
      cart[index].num++;
    }
    //5 吧购物车重新添加回缓存中
    wx.setStorageSync("cart", cart);
    //6 弹窗提示
    wx.showToast({
      title: '加入成功',
      icon: 'success',
      //true 防止用户手抖 疯狂点击按钮
      mask: true
    })
    console.log(this.GoodsInfo)
  }
})