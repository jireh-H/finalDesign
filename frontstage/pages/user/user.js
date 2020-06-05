// pages/user/user.js

import { request } from "../../service/network.js"

Page({

  /**
   * 页面的初始数据
   */
  data: {
    userInfo: [],
    isVIP:0,
    integral:0,
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    const userInfo = wx.getStorageSync("userinfo");
    const userid = wx.getStorageSync('userid');
    request({ url:'updatalogin', data:{ userid }})
    .then(res=>{
      console.log(res)
      const isVIP = res.data.isVIP;
      const integral = res.data.integral;
      wx.setStorageSync('isVIP', isVIP);
      wx.setStorageSync('integral', integral);
      this.setData({
        userInfo,
        isVIP,
        integral
      })
    })
  }
})