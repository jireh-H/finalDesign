// pages/login/login.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },
  //登录
  handleGetUserinfo(e) {
    const { userInfo } = e.detail;
    wx.setStorageSync("userinfo", userInfo);
    const name = e.detail.userInfo.nickName;
    const photo = e.detail.userInfo.avatarUrl;
    const loginParams = {
      name: name,
      photo: photo
    };
    wx.request({
      url: 'http://127.0.0.1:8000/frontstage/login/',
      data: loginParams,
      header: { "Content-Type": "application/x-www-form-urlencoded" },
      method: 'POST',
      dataType: 'json',
      success: function(res) {
        const userid = res.data.userid;
        const isVIP = res.data.isVIP;
        const integral = res.data.integral;
        wx.setStorageSync('userid', userid);
        wx.setStorageSync('isVIP', isVIP);
        wx.setStorageSync('integral', integral);
        wx.navigateBack({
          delta: 1
        });
      },
      fail: function(res) {},
      complete: function(res) {},
    })
    
  }

})