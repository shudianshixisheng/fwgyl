<template>
	<view class="verify-container">
		<!-- 导航栏 -->
		<view class="nav-bar">
			<view class="nav-back" @click="goBack">
				<text class="back-arrow">‹</text>
			</view>
			<text class="nav-title">实名认证</text>
			<view class="nav-placeholder"></view>
		</view>
		
		<!-- 表单 -->
		<view class="form-card">
			<view class="form-item">
				<text class="form-label">真实姓名</text>
				<input 
					class="form-input" 
					type="text" 
					v-model="name" 
					placeholder="请输入真实姓名"
					placeholder-class="placeholder"
				/>
			</view>
			
			<view class="form-item">
				<text class="form-label">身份证号</text>
				<input 
					class="form-input" 
					type="idcard" 
					v-model="idcard" 
					placeholder="请输入18位身份证号"
					placeholder-class="placeholder"
					maxlength="18"
				/>
			</view>
		</view>
		
		<!-- 提示 -->
		<view class="tips-card">
			<text class="tips-title">温馨提示</text>
			<text class="tips-text">• 实名认证信息将用于房产交易身份验证</text>
			<text class="tips-text">• 请确保填写的信息与身份证一致</text>
			<text class="tips-text">• 认证通过后将无法修改</text>
		</view>
		
		<!-- 提交按钮 -->
		<view class="submit-btn" :class="{ disabled: !canSubmit }" @click="handleSubmit">
			<text class="submit-text">{{ loading ? '提交中...' : '提交认证' }}</text>
		</view>
	</view>
</template>

<script>
import { submitVerify } from '@/utils/api.js';

export default {
	data() {
		return {
			name: '',
			idcard: '',
			loading: false
		}
	},
	computed: {
		canSubmit() {
			return this.name.length >= 2 && this.idcard.length === 18 && !this.loading;
		}
	},
	methods: {
		goBack() {
			uni.navigateBack();
		},
		async handleSubmit() {
			if (!this.canSubmit) return;
			
			// 验证身份证格式
			const idcardReg = /^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]$/;
			if (!idcardReg.test(this.idcard)) {
				uni.showToast({
					title: '请输入正确的身份证号',
					icon: 'none'
				});
				return;
			}
			
			this.loading = true;
			uni.showLoading({ title: '认证中...' });
			
			try {
				await submitVerify(this.name, this.idcard);
				
				uni.hideLoading();
				uni.showToast({
					title: '认证成功',
					icon: 'success'
				});
				
				setTimeout(() => {
					uni.navigateBack();
				}, 1500);
			} catch (err) {
				uni.hideLoading();
				uni.showToast({
					title: err.message || '认证失败',
					icon: 'none'
				});
			} finally {
				this.loading = false;
			}
		}
	}
}
</script>

<style scoped>
.verify-container {
	min-height: 100vh;
	background-color: #f5f7fa;
}

/* 导航栏 */
.nav-bar {
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

.nav-title {
	font-size: 34rpx;
	color: #1f2937;
	font-weight: 500;
}

.nav-placeholder {
	width: 60rpx;
}

/* 表单卡片 */
.form-card {
	margin: 24rpx;
	background-color: #ffffff;
	border-radius: 16rpx;
	padding: 16rpx 32rpx;
}

.form-item {
	display: flex;
	align-items: center;
	padding: 28rpx 0;
	border-bottom: 1rpx solid #f3f4f6;
}

.form-item:last-child {
	border-bottom: none;
}

.form-label {
	width: 160rpx;
	font-size: 30rpx;
	color: #374151;
	flex-shrink: 0;
}

.form-input {
	flex: 1;
	font-size: 30rpx;
	color: #1f2937;
	text-align: right;
}

.placeholder {
	color: #d1d5db;
}

/* 提示卡片 */
.tips-card {
	margin: 24rpx;
	padding: 24rpx;
	background-color: #fef3c7;
	border-radius: 12rpx;
}

.tips-title {
	display: block;
	font-size: 28rpx;
	color: #92400e;
	font-weight: 500;
	margin-bottom: 12rpx;
}

.tips-text {
	display: block;
	font-size: 24rpx;
	color: #a16207;
	line-height: 1.8;
}

/* 提交按钮 */
.submit-btn {
	margin: 48rpx 24rpx;
	background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
	border-radius: 16rpx;
	padding: 28rpx;
	display: flex;
	justify-content: center;
}

.submit-btn.disabled {
	background: #d1d5db;
}

.submit-text {
	font-size: 32rpx;
	color: #ffffff;
	font-weight: 500;
}
</style>
