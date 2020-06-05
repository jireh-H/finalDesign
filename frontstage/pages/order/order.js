// pages/order/order.js

import { request } from "../../service/network.js"

Page({

  /**
   * 页面的初始数据
   */
  data: {
    orders:[]
  },
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    const userid=wx.getStorageSync('userid')
    if(!userid){
      wx.navigateTo({
        url: '/pages/login/login',
      });
      return;
    }

    this.getOrderInfo(userid)
  },
  //获取全部订单信息
  getOrderInfo(userid){
    request({ url:"getOrderInfo", data:{userid:userid}})
    .then(res=>{
      let orders = res.data.message;
      this.setData({
        orders
      })
    })
  }

  
})