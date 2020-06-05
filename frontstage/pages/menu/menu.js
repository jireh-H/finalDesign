// pages/menu/menu.js

import { request } from "../../service/network.js"

Page({

  /**
   * 页面的初始数据
   */
  data: {
    //左侧的菜单数据
    leftMenuList: [],
    //右边的商品数据
    rightContent: [],
    //被点击的左侧的菜单
    currentIndex: 0,
    //每次点击距离上边框的距离
    scroll_top: 0,
    //菜品对象
    goodsObj: {},
  },
  Cates:[],
  //菜品对象
  GoodsInfo: {},

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
    //1. 获取本地存储中的数据 （小程序也是存在本地存储技术）
    const Cates = wx.getStorageSync("cates");
    //2. 判断
    if (!Cates) {
      this.getCates();
    } else {
      //有旧的数据 定义过期时间
      if (Date.now() - Cates.time > 1000 * 600) {
        this.getCates();
      } else {
        this.Cates = Cates.data;
        let leftMenuList = this.Cates.map(v => v.category);
        let rightContent = this.Cates[0].child;
        this.setData({
          leftMenuList,
          rightContent
        })
      }
    }
  },

  //获取分类数据
  getCates() {
    request({ url: 'menuInfo' })
      .then(res => {
        this.Cates = res.data.message;
        //把接口的数据存入到本地存储中
        wx.setStorageSync("cates", { time: Date.now(), data: this.Cates });
        //构造左侧大菜单数据
        let leftMenuList = this.Cates.map(v => v.category);
        //构造右侧的商品数据
        let rightContent = this.Cates[0].child;
        this.setData({
          leftMenuList,
          rightContent
        })
      })
  },

  //左侧菜单的点击事件
  handleItemTap(e) {
    //1.获取被点击的标题身上的索引
    //2.给data中的currentIndex赋值就可以了
    //3.根据不同的索引来渲染右侧的商品内容
    const { index } = e.currentTarget.dataset;
    let rightContent = this.Cates[index].child;
    this.setData({
      currentIndex: index,
      rightContent,
      //重新设置右侧内容的scroll-view标签的距离顶部的距离
      scroll_top: 0
    })
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})