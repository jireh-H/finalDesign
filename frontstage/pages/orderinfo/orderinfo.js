// pages/orderinfo/orderinfo.js

import { request } from "../../service/network.js"

Page({

  /**
   * 页面的初始数据
   */
  data: {
    ordersObj: {},
    orderObj:{},
  },


  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    let pages = getCurrentPages();
    let currentPage = pages[pages.length - 1];
    let options = currentPage.options;
    const { id } = options;
    this.getOrderinfo(id);
    this.getOrderDetail(id);
  },

  //获取订单信息
  getOrderinfo(id){
    request({ url:'getOrder' ,data:{ id } })
    .then(res=>{
      this.setData({
        orderObj:res.data.message
      })
    })
  },

  //获取订单详情
  getOrderDetail(id){
    request({ url: 'orderinfo', data: { id } })
    .then(res=>{
      console.log(res)
      this.setData({
        ordersObj : res.data.message
      })
    })
  }

  
})