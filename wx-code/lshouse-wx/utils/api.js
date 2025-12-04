/**
 * API 接口服务
 * Base URL: https://cuizy.online/lsszjj
 */

const BASE_URL = 'https://cuizy.online/lsszjj';

// 获取存储的 Token
const getToken = () => {
	return uni.getStorageSync('access_token') || '';
};

// 保存 Token
const saveToken = (accessToken, refreshToken) => {
	uni.setStorageSync('access_token', accessToken);
	uni.setStorageSync('refresh_token', refreshToken);
};

// 清除 Token
const clearToken = () => {
	uni.removeStorageSync('access_token');
	uni.removeStorageSync('refresh_token');
	uni.removeStorageSync('userInfo');
};

// 通用请求方法
const request = (url, method, data = {}, needAuth = true) => {
	return new Promise((resolve, reject) => {
		const header = {
			'Content-Type': 'application/json'
		};
		
		if (needAuth) {
			const token = getToken();
			if (token) {
				header['Authorization'] = `Bearer ${token}`;
			}
		}
		
		uni.request({
			url: BASE_URL + url,
			method,
			data,
			header,
			success: (res) => {
				if (res.data.code === 200) {
					resolve(res.data);
				} else if (res.data.code === 403) {
					// Token 无效，跳转登录
					clearToken();
					uni.showToast({
						title: '登录已过期，请重新登录',
						icon: 'none'
					});
					setTimeout(() => {
						uni.reLaunch({
							url: '/pages/login/login'
						});
					}, 1500);
					reject(res.data);
				} else {
					reject(res.data);
				}
			},
			fail: (err) => {
				uni.showToast({
					title: '网络请求失败',
					icon: 'none'
				});
				reject(err);
			}
		});
	});
};

// ============ 接口方法 ============

/**
 * 1. 登录
 * @param {string} username - 手机号
 * @param {string} password - 密码或验证码
 * @param {string} method - 登录方式：0-密码登录，1-短信登录
 */
export const login = (username, password, method = '1') => {
	return request('/auth/login', 'POST', {
		username,
		password,
		method,
		platform: '1' // 1-小程序
	}, false);
};

/**
 * 2. 发送短信验证码
 * @param {string} phone - 手机号
 * @param {string} type - 验证码类型：1-注册，2-登录
 */
export const sendSmsCode = (phone, type = '2') => {
	return request(`/auth/sms/send?phone=${phone}&type=${type}`, 'POST', {}, false);
};

/**
 * 3. 注册
 * @param {object} data - 注册信息
 */
export const register = (data) => {
	return request('/auth/register', 'POST', data, false);
};

/**
 * 4. 获取个人信息
 */
export const getUserInfo = () => {
	return request('/user/user/current/info', 'GET');
};

/**
 * 5. 更新个人信息
 * @param {object} data - 更新的字段
 */
export const updateUserInfo = (data) => {
	return request('/user/profile/update', 'PUT', data);
};

/**
 * 6. 获取实名认证状态
 */
export const getVerifyStatus = () => {
	return request('/user/verify/status', 'GET');
};

/**
 * 7. 提交实名认证
 * @param {string} name - 真实姓名
 * @param {string} idcard - 身份证号
 */
export const submitVerify = (name, idcard) => {
	return request('/user/verify/idcard', 'POST', { name, idcard });
};

// 导出工具方法
export { getToken, saveToken, clearToken };

export default {
	login,
	sendSmsCode,
	register,
	getUserInfo,
	updateUserInfo,
	getVerifyStatus,
	submitVerify,
	getToken,
	saveToken,
	clearToken
};
