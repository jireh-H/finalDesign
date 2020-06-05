// pages/sign/sign.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userphone:'',
    isVIP:0,
  },  
  formSubmit: function (e) {
    const userphone = e.detail.value.sign_phone;
    const userid = wx.getStorageSync('userid')
    const signParams = {
      userid: userid,
      userphone: userphone
    };
    wx.request({
      url: 'http://127.0.0.1:8000/frontstage/sign/',
      data: signParams,
      header: { "Content-Type": "application/x-www-form-urlencoded" },
      method: 'POST',
      dataType: 'json',
      success: function (res) {
        console.log(res)
        const isVIP =1;
        wx.setStorageSync('isVIP', isVIP);
        wx.navigateBack({
          delta: 1
        });
      },
      fail: function (res) {
        console.log(res)
      },
    })
  },


})