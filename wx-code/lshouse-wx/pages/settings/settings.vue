<template>
	<view class="settings-container">
		<!-- 导航栏 -->
		<view class="nav-bar">
			<view class="nav-back" @click="goBack">
				<text class="back-arrow">‹</text>
			</view>
			<text class="nav-title">设置</text>
			<view class="nav-placeholder"></view>
		</view>
		
		<!-- 账户信息 -->
		<view class="settings-card">
			<text class="card-title">账户信息</text>
			
			<view class="settings-list">
				<view class="settings-item" @click="editAvatar">
					<text class="item-label">头像</text>
					<view class="item-right">
						<view class="avatar-small">
							<view class="avatar-icon"></view>
						</view>
						<text class="item-arrow">›</text>
					</view>
				</view>
				
				<view class="settings-item" @click="editNickname">
					<text class="item-label">昵称</text>
					<view class="item-right">
						<text class="item-value">{{ userName }}</text>
						<text class="item-arrow">›</text>
					</view>
				</view>
				
				<view class="settings-item" @click="editPhone">
					<text class="item-label">手机号</text>
					<view class="item-right">
						<text class="item-value">{{ maskedPhone }}</text>
						<text class="item-arrow">›</text>
					</view>
				</view>
				
				<view class="settings-item" @click="goToVerify">
					<text class="item-label">实名认证</text>
					<view class="item-right">
						<view class="verified-status" v-if="isVerified">
							<view class="verified-icon"></view>
							<text class="verified-text">已认证</text>
						</view>
						<text class="item-value" v-else>未认证</text>
						<text class="item-arrow">›</text>
					</view>
				</view>
			</view>
		</view>
		
		<!-- 退出登录 -->
		<view class="logout-card" @click="handleLogout">
			<text class="logout-text">退出登录</text>
		</view>
		
		<!-- TabBar -->
		<view class="tabbar">
			<view class="tabbar-item" @click="goToHome">
				<view class="tabbar-icon icon-home"></view>
				<text class="tabbar-text">首页</text>
			</view>
			<view class="tabbar-item">
				<view class="tabbar-icon icon-find"></view>
				<text class="tabbar-text">找房</text>
			</view>
			<view class="tabbar-item">
				<view class="tabbar-icon icon-map"></view>
				<text class="tabbar-text">地图</text>
			</view>
			<view class="tabbar-item active">
				<view class="tabbar-icon icon-mine-active"></view>
				<text class="tabbar-text active">我的</text>
			</view>
		</view>
	</view>
</template>

<script>
import { getUserInfo, getVerifyStatus, clearToken } from '@/utils/api.js';

export default {
	data() {
		return {
			userInfo: null,
			isVerified: false,
			verifyInfo: null
		}
	},
	computed: {
		userName() {
			if (this.verifyInfo?.idcard_name) {
				return this.verifyInfo.idcard_name;
			}
			if (this.userInfo?.name) {
				return this.userInfo.name;
			}
			return '未设置';
		},
		maskedPhone() {
			const phone = this.userInfo?.phone || '';
			if (phone.length === 11) {
				return phone.substring(0, 3) + '****' + phone.substring(7);
			}
			return phone || '未绑定';
		}
	},
	onShow() {
		this.loadUserData();
	},
	methods: {
		async loadUserData() {
			// 从缓存读取
			const cachedUser = uni.getStorageSync('userInfo');
			if (cachedUser) {
				this.userInfo = cachedUser;
			}
			
			// 获取最新用户信息
			try {
				const res = await getUserInfo();
				this.userInfo = res.data;
				uni.setStorageSync('userInfo', res.data);
			} catch (err) {
				console.log('获取用户信息失败', err);
			}
			
			// 获取实名状态
			try {
				const verifyRes = await getVerifyStatus();
				this.isVerified = verifyRes.data.is_verified;
				this.verifyInfo = verifyRes.data;
			} catch (err) {
				console.log('获取实名状态失败', err);
			}
		},
		goBack() {
			uni.navigateBack();
		},
		goToHome() {
			uni.reLaunch({
				url: '/pages/index/index'
			});
		},
		editAvatar() {
			uni.showToast({ title: '修改头像', icon: 'none' });
		},
		editNickname() {
			uni.showToast({ title: '修改昵称', icon: 'none' });
		},
		editPhone() {
			uni.showToast({ title: '修改手机号', icon: 'none' });
		},
		goToVerify() {
			if (this.isVerified) {
				uni.showToast({ title: '已完成实名认证', icon: 'none' });
			} else {
				uni.navigateTo({
					url: '/pages/verify/verify'
				});
			}
		},
		handleLogout() {
			uni.showModal({
				title: '提示',
				content: '确定要退出登录吗？',
				success: (res) => {
					if (res.confirm) {
						clearToken();
						uni.reLaunch({
							url: '/pages/login/login'
						});
					}
				}
			});
		}
	}
}
</script>

<style scoped>
.settings-container {
	min-height: 100vh;
	background-color: #f5f7fa;
	padding-bottom: 120rpx;
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

/* 设置卡片 */
.settings-card {
	margin: 24rpx;
	background-color: #ffffff;
	border-radius: 16rpx;
	padding: 32rpx;
}

.card-title {
	font-size: 28rpx;
	color: #3b82f6;
	margin-bottom: 16rpx;
}

.settings-list {
	display: flex;
	flex-direction: column;
}

.settings-item {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 28rpx 0;
	border-bottom: 1rpx solid #f3f4f6;
}

.settings-item:last-child {
	border-bottom: none;
}

.item-label {
	font-size: 30rpx;
	color: #374151;
}

.item-right {
	display: flex;
	align-items: center;
	gap: 16rpx;
}

.avatar-small {
	width: 64rpx;
	height: 64rpx;
	background-color: #f3f4f6;
	border-radius: 50%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.avatar-icon {
	width: 36rpx;
	height: 36rpx;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Cpath d='M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2'/%3E%3Ccircle cx='12' cy='7' r='4'/%3E%3C/svg%3E");
	background-size: contain;
	background-repeat: no-repeat;
	background-position: center;
}

.item-value {
	font-size: 28rpx;
	color: #9ca3af;
}

.item-arrow {
	font-size: 32rpx;
	color: #d1d5db;
}

.verified-status {
	display: flex;
	align-items: center;
	gap: 8rpx;
}

.verified-icon {
	width: 28rpx;
	height: 28rpx;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='%2322c55e' stroke='%2322c55e' stroke-width='2'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Cpath d='m9 12 2 2 4-4' stroke='white' stroke-width='2'/%3E%3C/svg%3E");
	background-size: contain;
	background-repeat: no-repeat;
}

.verified-text {
	font-size: 28rpx;
	color: #22c55e;
}

/* 退出登录 */
.logout-card {
	margin: 24rpx;
	background-color: #ffffff;
	border-radius: 16rpx;
	padding: 32rpx;
	display: flex;
	justify-content: center;
}

.logout-text {
	font-size: 30rpx;
	color: #ef4444;
}

/* TabBar */
.tabbar {
	position: fixed;
	bottom: 0;
	left: 0;
	right: 0;
	display: flex;
	justify-content: space-around;
	align-items: center;
	height: 110rpx;
	background-color: #ffffff;
	border-top: 1rpx solid #f3f4f6;
	padding-bottom: env(safe-area-inset-bottom);
}

.tabbar-item {
	display: flex;
	flex-direction: column;
	align-items: center;
	padding: 10rpx 0;
}

.tabbar-icon {
	width: 48rpx;
	height: 48rpx;
	margin-bottom: 6rpx;
	background-size: contain;
	background-repeat: no-repeat;
	background-position: center;
}

.icon-home {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Cpath d='m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'/%3E%3Cpolyline points='9 22 9 12 15 12 15 22'/%3E%3C/svg%3E");
}

.icon-find {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Crect width='16' height='20' x='4' y='2' rx='2' ry='2'/%3E%3Cpath d='M9 22v-4h6v4'/%3E%3Cpath d='M8 6h.01'/%3E%3Cpath d='M16 6h.01'/%3E%3Cpath d='M12 6h.01'/%3E%3Cpath d='M12 10h.01'/%3E%3Cpath d='M12 14h.01'/%3E%3Cpath d='M16 10h.01'/%3E%3Cpath d='M16 14h.01'/%3E%3Cpath d='M8 10h.01'/%3E%3Cpath d='M8 14h.01'/%3E%3C/svg%3E");
}

.icon-map {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Cpolygon points='3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21'/%3E%3Cline x1='9' x2='9' y1='3' y2='18'/%3E%3Cline x1='15' x2='15' y1='6' y2='21'/%3E%3C/svg%3E");
}

.icon-mine-active {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='%232563eb' stroke='%232563eb' stroke-width='2'%3E%3Cpath d='M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2'/%3E%3Ccircle cx='12' cy='7' r='4'/%3E%3C/svg%3E");
}

.tabbar-text {
	font-size: 22rpx;
	color: #9ca3af;
}

.tabbar-text.active {
	color: #2563eb;
}
</style>
