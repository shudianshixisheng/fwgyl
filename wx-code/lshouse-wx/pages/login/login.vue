<template>
	<view class="login-container">
		<!-- Hero Section -->
		<view class="hero-section">
			<!-- Background Image -->
			<image 
				class="hero-bg" 
				src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&q=80" 
				mode="aspectFill"
			/>
			<!-- Gradient Overlay -->
			<view class="hero-overlay"></view>
			
			<!-- Hero Content -->
			<view class="hero-content">
				<!-- Logo Area -->
				<view class="logo-row">
					<view class="logo-icon-box">
						<!-- Building Icon -->
						<view class="building-icon">
							<text class="iconfont icon-building"></text>
						</view>
					</view>
					<view class="logo-text">
						<text class="app-title">陵水好房</text>
						<text class="app-subtitle">Lingshui Housing</text>
					</view>
				</view>
				
				<!-- Tagline -->
				<view class="tagline-area">
					<text class="tagline-main">一码两链，诚信交易</text>
					<text class="tagline-sub">海南省现房交易示范项目</text>
				</view>
			</view>
			
			<!-- Badges -->
			<view class="badges-row">
				<view class="badge-item">
					<view class="badge-icon shield-icon"></view>
					<text class="badge-text">住建局监管</text>
				</view>
				<view class="badge-item">
					<view class="badge-icon check-icon"></view>
					<text class="badge-text">两保两真</text>
				</view>
			</view>
		</view>
		
		<!-- Form Section -->
		<view class="form-section">
			<text class="form-title">手机号登录</text>
			
			<!-- Phone Input -->
			<view class="input-group">
				<text class="input-label">手机号码</text>
				<view class="input-wrapper">
					<input 
						type="number" 
						v-model="phone" 
						placeholder="请输入11位手机号" 
						maxlength="11"
						class="input-field"
					/>
				</view>
			</view>
			
			<!-- SMS Code Input -->
			<view class="input-group">
				<text class="input-label">短信验证码</text>
				<view class="code-row">
					<view class="input-wrapper code-input-box">
						<input 
							type="number" 
							v-model="smsCode" 
							placeholder="请输入验证码" 
							maxlength="6"
							class="input-field"
						/>
					</view>
					<view 
						class="get-code-btn" 
						:class="{ disabled: countdown > 0 }"
						@click="getCode"
					>
						<text class="get-code-text">{{ countdown > 0 ? `${countdown}s` : '获取验证码' }}</text>
					</view>
				</view>
			</view>
			
			<!-- Login Button -->
			<button class="login-btn" @click="handleLogin">
				<text class="login-btn-text">登录</text>
			</button>
			
			<!-- Agreement -->
			<view class="agreement-row">
				<view 
					class="checkbox-wrapper" 
					@click="agreeChecked = !agreeChecked"
				>
					<view class="checkbox" :class="{ checked: agreeChecked }">
						<text v-if="agreeChecked" class="check-mark">✓</text>
					</view>
				</view>
				<view class="agreement-text">
					<text class="agreement-normal">登录即表示同意</text>
					<text class="agreement-link" @click="openAgreement('user')">《用户服务协议》</text>
					<text class="agreement-normal">和</text>
					<text class="agreement-link" @click="openAgreement('privacy')">《隐私保护政策》</text>
				</view>
			</view>
			
			<!-- Register Link -->
			<view class="register-link" @click="goToRegister">
				<text class="register-link-text">没有账号？</text>
				<text class="register-link-action">立即注册</text>
			</view>
		</view>
		
		<!-- Footer -->
		<view class="footer">
			<text class="footer-text">陵水房协运营</text>
			<text class="footer-dot">·</text>
			<text class="footer-text">陵水数投技术支持</text>
		</view>
	</view>
</template>

<script>
import { login, sendSmsCode, saveToken, getUserInfo } from '@/utils/api.js';

export default {
	data() {
		return {
			phone: '',
			smsCode: '',
			countdown: 0,
			agreeChecked: false,
			timer: null,
			loading: false
		}
	},
	methods: {
		async getCode() {
			if (this.countdown > 0) return;
			
			if (!this.phone || this.phone.length !== 11) {
				uni.showToast({
					title: '请输入正确的手机号',
					icon: 'none'
				});
				return;
			}
			
			try {
				// 调用发送验证码接口
				await sendSmsCode(this.phone, '2');
				
				// 开始倒计时
				this.countdown = 60;
				this.timer = setInterval(() => {
					this.countdown--;
					if (this.countdown <= 0) {
						clearInterval(this.timer);
					}
				}, 1000);
				
				uni.showToast({
					title: '验证码已发送',
					icon: 'success'
				});
			} catch (err) {
				uni.showToast({
					title: err.message || '发送失败',
					icon: 'none'
				});
			}
		},
		
		async handleLogin() {
			if (!this.phone || this.phone.length !== 11) {
				uni.showToast({
					title: '请输入正确的手机号',
					icon: 'none'
				});
				return;
			}
			
			if (!this.smsCode || this.smsCode.length < 4) {
				uni.showToast({
					title: '请输入验证码',
					icon: 'none'
				});
				return;
			}
			
			if (!this.agreeChecked) {
				uni.showToast({
					title: '请阅读并同意用户协议',
					icon: 'none'
				});
				return;
			}
			
			if (this.loading) return;
			this.loading = true;
			
			uni.showLoading({ title: '登录中...' });
			
			try {
				// 调用登录接口 (短信验证码登录)
				const res = await login(this.phone, this.smsCode, '1');
				
				// 保存 Token
				saveToken(res.data.access_token, res.data.refresh_token);
				
				// 获取用户信息并缓存
				try {
					const userRes = await getUserInfo();
					uni.setStorageSync('userInfo', userRes.data);
				} catch (e) {
					console.log('获取用户信息失败', e);
				}
				
				uni.hideLoading();
				uni.showToast({
					title: '登录成功',
					icon: 'success'
				});
				
				// 跳转到首页
				setTimeout(() => {
					uni.reLaunch({
						url: '/pages/index/index'
					});
				}, 1500);
			} catch (err) {
				uni.hideLoading();
				uni.showToast({
					title: err.message || '登录失败',
					icon: 'none'
				});
			} finally {
				this.loading = false;
			}
		},
		
		openAgreement(type) {
			uni.showToast({
				title: type === 'user' ? '用户服务协议' : '隐私保护政策',
				icon: 'none'
			});
		},
		goToRegister() {
			uni.navigateTo({
				url: '/pages/register/register'
			});
		}
	},
	
	onUnload() {
		if (this.timer) {
			clearInterval(this.timer);
		}
	}
}
</script>

<style scoped>
.login-container {
	min-height: 100vh;
	background-color: #ffffff;
	display: flex;
	flex-direction: column;
}

/* Hero Section */
.hero-section {
	position: relative;
	height: 42vh;
	min-height: 580rpx;
	overflow: visible;
}

.hero-bg {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: calc(100% + 40rpx);
}

.hero-overlay {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: -40rpx;
	background: linear-gradient(
		to bottom,
		rgba(30, 64, 175, 0.65) 0%,
		rgba(37, 99, 235, 0.45) 60%,
		rgba(59, 130, 246, 0.2) 100%
	);
}

.hero-content {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	padding: 96rpx 48rpx 0;
}

/* Logo Row */
.logo-row {
	display: flex;
	align-items: center;
	gap: 24rpx;
	margin-bottom: 32rpx;
}

.logo-icon-box {
	width: 96rpx;
	height: 96rpx;
	background-color: rgba(255, 255, 255, 0.95);
	border-radius: 28rpx;
	display: flex;
	align-items: center;
	justify-content: center;
	box-shadow: 0 20rpx 30rpx -6rpx rgba(0, 0, 0, 0.1), 
	            0 8rpx 12rpx -8rpx rgba(0, 0, 0, 0.1);
}

.building-icon {
	width: 56rpx;
	height: 56rpx;
	display: flex;
	align-items: center;
	justify-content: center;
}

.building-icon::before {
	content: '';
	width: 44rpx;
	height: 44rpx;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%232563eb' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M10 12h4'%3E%3C/path%3E%3Cpath d='M10 8h4'%3E%3C/path%3E%3Cpath d='M14 21v-3a2 2 0 0 0-4 0v3'%3E%3C/path%3E%3Cpath d='M6 10H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-2'%3E%3C/path%3E%3Cpath d='M6 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16'%3E%3C/path%3E%3C/svg%3E");
	background-size: contain;
	background-repeat: no-repeat;
	background-position: center;
}

.logo-text {
	display: flex;
	flex-direction: column;
}

.app-title {
	font-size: 48rpx;
	color: #ffffff;
	letter-spacing: 4rpx;
	line-height: 1.3;
}

.app-subtitle {
	font-size: 24rpx;
	color: rgba(255, 255, 255, 0.9);
	margin-top: 4rpx;
}

/* Tagline */
.tagline-area {
	margin-top: 64rpx;
}

.tagline-main {
	display: block;
	font-size: 36rpx;
	color: #ffffff;
	line-height: 1.5;
}

.tagline-sub {
	display: block;
	font-size: 28rpx;
	color: rgba(255, 255, 255, 0.8);
	margin-top: 8rpx;
}

/* Badges */
.badges-row {
	position: absolute;
	bottom: 40rpx;
	left: 48rpx;
	right: 48rpx;
	display: flex;
	gap: 16rpx;
}

.badge-item {
	display: flex;
	align-items: center;
	gap: 12rpx;
	background-color: rgba(255, 255, 255, 0.2);
	backdrop-filter: blur(8rpx);
	padding: 12rpx 24rpx;
	border-radius: 100rpx;
}

.badge-icon {
	width: 28rpx;
	height: 28rpx;
	background-size: contain;
	background-repeat: no-repeat;
	background-position: center;
}

.shield-icon {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z'%3E%3C/path%3E%3C/svg%3E");
}

.check-icon {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpath d='m9 12 2 2 4-4'%3E%3C/path%3E%3C/svg%3E");
}

.badge-text {
	font-size: 24rpx;
	color: #ffffff;
	line-height: 1;
}

/* Form Section */
.form-section {
	flex: 1;
	padding: 48rpx;
	padding-top: 40rpx;
	background-color: #ffffff;
	border-top-left-radius: 40rpx;
	border-top-right-radius: 40rpx;
	margin-top: -40rpx;
	position: relative;
	z-index: 10;
}

.form-title {
	font-size: 40rpx;
	color: #1a365d;
	font-weight: 500;
	margin-bottom: 40rpx;
}

.input-group {
	margin-bottom: 32rpx;
}

.input-label {
	display: block;
	font-size: 28rpx;
	color: #475569;
	margin-bottom: 16rpx;
	font-weight: 400;
}

.input-wrapper {
	border: 2rpx solid #e5e7eb;
	border-radius: 16rpx;
	overflow: hidden;
	background-color: #ffffff;
}

.input-field {
	width: 100%;
	height: 88rpx;
	padding: 0 28rpx;
	font-size: 30rpx;
	color: #1f2937;
	background-color: transparent;
}

.input-field::placeholder {
	color: #9ca3af;
}

.code-row {
	display: flex;
	align-items: center;
	gap: 20rpx;
}

.code-input-box {
	flex: 1;
}

.get-code-btn {
	padding: 0 32rpx;
	height: 96rpx;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color: transparent;
}

.get-code-btn.disabled {
	opacity: 0.6;
}

.get-code-text {
	font-size: 32rpx;
	color: #3b82f6;
	white-space: nowrap;
}

/* Login Button */
.login-btn {
	width: 100%;
	height: 100rpx;
	background: linear-gradient(135deg, #93c5fd 0%, #60a5fa 100%);
	border-radius: 50rpx;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-top: 40rpx;
	border: none;
}

.login-btn::after {
	border: none;
}

.login-btn-text {
	font-size: 32rpx;
	color: rgba(255, 255, 255, 0.95);
	font-weight: 400;
}

/* Agreement */
.agreement-row {
	display: flex;
	align-items: flex-start;
	margin-top: 36rpx;
	padding: 0;
}

.checkbox-wrapper {
	padding-top: 4rpx;
	margin-right: 16rpx;
}

.checkbox {
	width: 32rpx;
	height: 32rpx;
	border: 2rpx solid #d1d5db;
	border-radius: 6rpx;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color: #ffffff;
}

.checkbox.checked {
	background-color: #2563eb;
	border-color: #2563eb;
}

.check-mark {
	font-size: 20rpx;
	color: #ffffff;
	font-weight: bold;
}

.agreement-text {
	flex: 1;
	line-height: 1.6;
}

.agreement-normal {
	font-size: 24rpx;
	color: #6b7280;
}

.agreement-link {
	font-size: 24rpx;
	color: #2563eb;
}

/* Register Link */
.register-link {
	display: flex;
	justify-content: center;
	gap: 8rpx;
	margin-top: 48rpx;
}

.register-link-text {
	font-size: 28rpx;
	color: #6b7280;
}

.register-link-action {
	font-size: 28rpx;
	color: #2563eb;
}

/* Footer */
.footer {
	display: flex;
	align-items: center;
	justify-content: center;
	padding: 28rpx 32rpx;
	border-top: 1rpx solid #f1f5f9;
	background-color: #ffffff;
}

.footer-text {
	font-size: 24rpx;
	color: #6b7280;
}

.footer-dot {
	font-size: 24rpx;
	color: #6b7280;
	margin: 0 16rpx;
}
</style>
