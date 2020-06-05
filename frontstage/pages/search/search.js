// pages/search/search.js

import { request } from "../../service/network.js"

Page({

  /**
   * 页面的初始数据
   */
  data: {
    foods: [],
    // 取消按钮是否显示
    isFocus: false,
    //输入框的值
    inpValue: ""
  },
  TimeId: -1,

  //输入框的值改变 就会触发的事件
  handleInput(e) {
    //1 获取输入框的值
    const { value } = e.detail;
    //2 检测合法性
    if (!value.trim()) {
      this.setData({
        foods: [],
        isFocus: false
      })
      //值不合法
      return;
    }
    //3 准备发送请求获取数据
    this.setData({
      isFocus: true
    })
    clearTimeout(this.TimeId);
    this.TimeId = setTimeout(() => {
      this.qsearch(value);
    }, 1000)
  },

  //发送请求获取搜索建议 数据
  qsearch(query) {
    request({ url: "qsearch", data: { query } })
      .then(res => {
        console.log(res)
        this.setData({
          goods: res.data.message
        })
      })
  },

  //点击取消按钮
  handleCancel() {
    this.setData({
      inpValue: "",
      isFocus: false,
      goods: []
    })
  }
})