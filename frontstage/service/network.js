
//定义一个网络请求次数
let ajaxTimes = 0;

export const request = (params) => {
  // 判断 url中是否带有/my/ 请求的是私有的路径 带上header token
  let header = { ...params.header };
  if (params.url.includes("/my/")) {
    // 拼接header 带上token
    header['Authorization'] = wx.getStorageSync("token");

  }

  ajaxTimes++;
  //显示加载中效果
  wx.showLoading({
    title: '加载中',
    mask: true
  });

  //定义公共的url
  const baseUrl = "http://127.0.0.1:8000/frontstage/";
  return new Promise((resolve, reject) => {
    wx.request({
      ...params,
      header: header,
      url: baseUrl + params.url,
      success: (res) => {
        resolve(res);
      },
      fail: (err) => {
        reject(err);
      },

      complete: () => {
        ajaxTimes--;
        if (ajaxTimes === 0) {
          wx.hideLoading();
        }

      }
    });

  })
}