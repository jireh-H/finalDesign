// pages/pay/pay.js

import { request } from "../../service/network.js"

/**
1 点击确认支付
  跳回上一页面
  发送post请求将购物车缓存发送给后端接受
  将购物车缓存清零
  
 */
Page({

  /**
   * 页面的初始数据
   */
  data: {
    cart:[],
    timestamp:0,
    userid:0,
  },

  onShow(){
    //1 获取缓存中的购物车数据
    let cart = wx.getStorageSync("cart") || [];
    //过滤后的购物车数组
    cart = cart.filter(v => v.checked);
    //1 总价格 总数量
    let totalPrice = 0;
    let totalNum = 0;
    cart.forEach(v => {
      totalPrice += v.num * v.price;
      totalNum += v.num;
    })
    this.setData({
      cart,
      totalPrice,
      totalNum,
    });
    wx.setStorageSync("cart", cart);
  },

  //点击支付
  handleOrderPay(){
    const userid = wx.getStorageSync('userid')
    if (!userid) {
      wx.navigateTo({
        url: '/pages/login/login',
      });
      return;
    }
    const order_price = this.data.totalPrice;
    const cart = this.data.cart;
    let goods=[]
    cart.forEach(v => goods.push({
      goods_id: v.id,
      goods_number: v.num,
      goods_price: v.price
    }))
    var timestamp = Date.parse(new Date());
    const orderParams = { 
        userid:userid,
        order_price:order_price, 
        goods:JSON.stringify(goods), 
        timestamp: timestamp
    };
    wx.request({
      url: 'http://127.0.0.1:8000/frontstage/createorder/',
      data: orderParams,
      header: { "Content-Type": "application/x-www-form-urlencoded" },
      method: 'POST',
      dataType: 'json',
      success: function(res) {
        wx.showToast({ title: '支付成功' });
        //8 手动删除缓存中已经支付了的商品
        let newCart = wx.getStorageSync("cart");
        newCart = newCart.filter(v => !v.checked);
        wx.setStorageSync("cart", newCart);
        // 8 支付成功了 跳转到订单页面
        wx.switchTab({
          url: '/pages/order/order',
        })
      },
      fail: function(res) {
        console.log(res)
      },
      complete: function(res) {
      },
    })
  }
})