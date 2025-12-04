<template>
	<view class="register-container">
		<!-- Header -->
		<view class="header">
			<view class="nav-back" @click="goBack">
				<text class="back-arrow">‹</text>
			</view>
			<text class="header-title">注册账号</text>
			<view class="nav-placeholder"></view>
		</view>
		
		<!-- Form -->
		<view class="form-section">
			<!-- 手机号 -->
			<view class="input-group">
				<text class="input-label">手机号</text>
				<view class="input-row">
					<text class="prefix">+86</text>
					<input 
						class="input-field" 
						type="number" 
						v-model="phone" 
						placeholder="请输入手机号"
						placeholder-class="placeholder"
						maxlength="11"
					/>
				</view>
			</view>
			
			<!-- 验证码 -->
			<view class="input-group">
				<text class="input-label">验证码</text>
				<view class="input-row">
					<input 
						class="input-field code-input" 
						type="number" 
						v-model="smsCode" 
						placeholder="请输入验证码"
						placeholder-class="placeholder"
						maxlength="6"
					/>
					<view class="code-btn" :class="{ disabled: countdown > 0 }" @click="getCode">
						<text class="code-btn-text">{{ countdown > 0 ? countdown + 's' : '获取验证码' }}</text>
					</view>
				</view>
			</view>
			
			<!-- 密码 -->
			<view class="input-group">
				<text class="input-label">设置密码</text>
				<view class="input-row">
					<input 
						class="input-field" 
						:type="showPassword ? 'text' : 'password'" 
						v-model="password" 
						placeholder="请设置6-20位密码"
						placeholder-class="placeholder"
						maxlength="20"
					/>
					<view class="eye-btn" @click="showPassword = !showPassword">
						<view class="eye-icon" :class="{ active: showPassword }"></view>
					</view>
				</view>
			</view>
			
			<!-- 确认密码 -->
			<view class="input-group">
				<text class="input-label">确认密码</text>
				<view class="input-row">
					<input 
						class="input-field" 
						:type="showPassword2 ? 'text' : 'password'" 
						v-model="passwordConfirm" 
						placeholder="请再次输入密码"
						placeholder-class="placeholder"
						maxlength="20"
					/>
					<view class="eye-btn" @click="showPassword2 = !showPassword2">
						<view class="eye-icon" :class="{ active: showPassword2 }"></view>
					</view>
				</view>
			</view>
			
			<!-- 邮箱 (可选) -->
			<view class="input-group">
				<text class="input-label">邮箱 <text class="optional">(选填)</text></text>
				<view class="input-row">
					<input 
						class="input-field" 
						type="text" 
						v-model="email" 
						placeholder="请输入邮箱"
						placeholder-class="placeholder"
					/>
				</view>
			</view>
			
			<!-- 性别 -->
			<view class="input-group">
				<text class="input-label">性别</text>
				<view class="gender-row">
					<view 
						class="gender-item" 
						:class="{ active: gender === '0' }" 
						@click="gender = '0'"
					>
						<text class="gender-text">男</text>
					</view>
					<view 
						class="gender-item" 
						:class="{ active: gender === '1' }" 
						@click="gender = '1'"
					>
						<text class="gender-text">女</text>
					</view>
				</view>
			</view>
		</view>
		
		<!-- Agreement -->
		<view class="agreement-row">
			<view class="checkbox-wrapper" @click="agreeChecked = !agreeChecked">
				<view class="checkbox" :class="{ checked: agreeChecked }">
					<text v-if="agreeChecked" class="check-mark">✓</text>
				</view>
			</view>
			<view class="agreement-text">
				<text class="agreement-normal">我已阅读并同意</text>
				<text class="agreement-link">《用户服务协议》</text>
				<text class="agreement-normal">和</text>
				<text class="agreement-link">《隐私保护政策》</text>
			</view>
		</view>
		
		<!-- Register Button -->
		<button class="register-btn" :class="{ disabled: !canSubmit }" @click="handleRegister">
			<text class="register-btn-text">{{ loading ? '注册中...' : '注册' }}</text>
		</button>
		
		<!-- Login Link -->
		<view class="login-link" @click="goToLogin">
			<text class="login-link-text">已有账号？</text>
			<text class="login-link-action">立即登录</text>
		</view>
	</view>
</template>

<script>
import { register, sendSmsCode, login, saveToken, getUserInfo } from '@/utils/api.js';

export default {
	data() {
		return {
			phone: '',
			smsCode: '',
			password: '',
			passwordConfirm: '',
			email: '',
			gender: '0',
			countdown: 0,
			timer: null,
			agreeChecked: false,
			showPassword: false,
			showPassword2: false,
			loading: false
		}
	},
	computed: {
		canSubmit() {
			return this.phone.length === 11 && 
				this.smsCode.length >= 4 && 
				this.password.length >= 6 && 
				this.passwordConfirm.length >= 6 &&
				this.agreeChecked &&
				!this.loading;
		}
	},
	methods: {
		goBack() {
			uni.navigateBack();
		},
		goToLogin() {
			uni.navigateBack();
		},
		async getCode() {
			if (this.countdown > 0) return;
			
			if (!this.phone || this.phone.length !== 11) {
				uni.showToast({ title: '请输入正确的手机号', icon: 'none' });
				return;
			}
			
			try {
				// type=1 为注册验证码
				await sendSmsCode(this.phone, '1');
				
				this.countdown = 60;
				this.timer = setInterval(() => {
					this.countdown--;
					if (this.countdown <= 0) {
						clearInterval(this.timer);
					}
				}, 1000);
				
				uni.showToast({ title: '验证码已发送', icon: 'success' });
			} catch (err) {
				uni.showToast({ title: err.message || '发送失败', icon: 'none' });
			}
		},
		async handleRegister() {
			if (!this.canSubmit) return;
			
			// 验证密码
			if (this.password !== this.passwordConfirm) {
				uni.showToast({ title: '两次密码输入不一致', icon: 'none' });
				return;
			}
			
			if (this.password.length < 6) {
				uni.showToast({ title: '密码至少6位', icon: 'none' });
				return;
			}
			
			this.loading = true;
			uni.showLoading({ title: '注册中...' });
			
			try {
				// 调用注册接口
				await register({
					phone: this.phone,
					email: this.email || undefined,
					gender: this.gender,
					sms_code: this.smsCode,
					password: this.password,
					password_two: this.passwordConfirm
				});
				
				uni.hideLoading();
				uni.showToast({ title: '注册成功', icon: 'success' });
				
				// 自动登录
				try {
					const loginRes = await login(this.phone, this.password, '0');
					saveToken(loginRes.data.access_token, loginRes.data.refresh_token);
					
					const userRes = await getUserInfo();
					uni.setStorageSync('userInfo', userRes.data);
					
					setTimeout(() => {
						uni.reLaunch({ url: '/pages/index/index' });
					}, 1500);
				} catch (e) {
					// 自动登录失败，跳转登录页
					setTimeout(() => {
						uni.reLaunch({ url: '/pages/login/login' });
					}, 1500);
				}
			} catch (err) {
				uni.hideLoading();
				uni.showToast({ title: err.message || '注册失败', icon: 'none' });
			} finally {
				this.loading = false;
			}
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
.register-container {
	min-height: 100vh;
	background-color: #f5f7fa;
	padding-bottom: 60rpx;
}

/* Header */
.header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 24rpx 32rpx;
	padding-top: calc(var(--status-bar-height) + 24rpx);
	background-color: #ffffff;
}

.nav-back {
	width: 60rpx;
	height: 60rpx;
	display: flex;
	align-items: center;
	justify-content: center;
}

.back-arrow {
	font-size: 48rpx;
	color: #374151;
	font-weight: 300;
}

.header-title {
	font-size: 34rpx;
	color: #1f2937;
	font-weight: 500;
}

.nav-placeholder {
	width: 60rpx;
}

/* Form */
.form-section {
	margin: 24rpx;
	background-color: #ffffff;
	border-radius: 16rpx;
	padding: 16rpx 32rpx;
}

.input-group {
	padding: 24rpx 0;
	border-bottom: 1rpx solid #f3f4f6;
}

.input-group:last-child {
	border-bottom: none;
}

.input-label {
	display: block;
	font-size: 28rpx;
	color: #6b7280;
	margin-bottom: 16rpx;
}

.optional {
	color: #9ca3af;
}

.input-row {
	display: flex;
	align-items: center;
	gap: 16rpx;
}

.prefix {
	font-size: 32rpx;
	color: #1f2937;
	padding-right: 16rpx;
	border-right: 1rpx solid #e5e7eb;
}

.input-field {
	flex: 1;
	font-size: 32rpx;
	color: #1f2937;
	height: 56rpx;
}

.code-input {
	flex: 1;
}

.placeholder {
	color: #d1d5db;
}

.code-btn {
	background-color: #eff6ff;
	padding: 16rpx 24rpx;
	border-radius: 8rpx;
}

.code-btn.disabled {
	background-color: #f3f4f6;
}

.code-btn-text {
	font-size: 26rpx;
	color: #2563eb;
}

.code-btn.disabled .code-btn-text {
	color: #9ca3af;
}

.eye-btn {
	padding: 10rpx;
}

.eye-icon {
	width: 40rpx;
	height: 40rpx;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Cpath d='M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24'/%3E%3Cline x1='1' x2='23' y1='1' y2='23'/%3E%3C/svg%3E");
	background-size: contain;
	background-repeat: no-repeat;
}

.eye-icon.active {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%232563eb' stroke-width='2'%3E%3Cpath d='M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/svg%3E");
}

/* Gender */
.gender-row {
	display: flex;
	gap: 24rpx;
}

.gender-item {
	flex: 1;
	padding: 20rpx;
	border: 2rpx solid #e5e7eb;
	border-radius: 12rpx;
	display: flex;
	justify-content: center;
}

.gender-item.active {
	border-color: #2563eb;
	background-color: #eff6ff;
}

.gender-text {
	font-size: 30rpx;
	color: #6b7280;
}

.gender-item.active .gender-text {
	color: #2563eb;
}

/* Agreement */
.agreement-row {
	display: flex;
	align-items: flex-start;
	padding: 24rpx 32rpx;
	gap: 12rpx;
}

.checkbox-wrapper {
	padding: 4rpx;
}

.checkbox {
	width: 36rpx;
	height: 36rpx;
	border: 2rpx solid #d1d5db;
	border-radius: 6rpx;
	display: flex;
	align-items: center;
	justify-content: center;
}

.checkbox.checked {
	background-color: #2563eb;
	border-color: #2563eb;
}

.check-mark {
	font-size: 24rpx;
	color: #ffffff;
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

/* Button */
.register-btn {
	margin: 32rpx;
	background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
	border-radius: 16rpx;
	padding: 28rpx;
	border: none;
}

.register-btn.disabled {
	background: #d1d5db;
}

.register-btn-text {
	font-size: 32rpx;
	color: #ffffff;
	font-weight: 500;
}

/* Login Link */
.login-link {
	display: flex;
	justify-content: center;
	gap: 8rpx;
	padding: 24rpx;
}

.login-link-text {
	font-size: 28rpx;
	color: #6b7280;
}

.login-link-action {
	font-size: 28rpx;
	color: #2563eb;
}
</style>
