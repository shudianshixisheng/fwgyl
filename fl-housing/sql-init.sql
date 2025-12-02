-- ============================================================
-- 陵水住房供应链平台 Day1初始化SQL
-- 数据库: MySQL 8.0+
-- ============================================================

CREATE DATABASE IF NOT EXISTS lingshui_housing DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE lingshui_housing;

-- 1.1 用户表
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `phone` VARCHAR(20) NOT NULL COMMENT '手机号',
    `username` VARCHAR(50) DEFAULT NULL COMMENT '用户名',
    `password_hash` VARCHAR(255) NOT NULL COMMENT '密码',
    `nickname` VARCHAR(50) DEFAULT NULL COMMENT '昵称',
    `avatar_url` VARCHAR(500) DEFAULT NULL COMMENT '头像',
    `user_level` ENUM('temp', 'normal', 'verified') NOT NULL DEFAULT 'normal' COMMENT '等级',
    `credit_score` INT DEFAULT NULL COMMENT '信用分',
    `status` ENUM('active', 'disabled', 'deleted') NOT NULL DEFAULT 'active',
    `last_login_at` DATETIME DEFAULT NULL,
    `last_login_ip` VARCHAR(50) DEFAULT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_phone` (`phone`),
    UNIQUE KEY `uk_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

-- 1.2 用户实名认证表
DROP TABLE IF EXISTS `user_verification`;
CREATE TABLE `user_verification` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT UNSIGNED NOT NULL,
    `verify_type` ENUM('idcard', 'credit_score', 'education') NOT NULL,
    `real_name` VARCHAR(50) DEFAULT NULL,
    `id_card_no` VARCHAR(255) DEFAULT NULL,
    `credit_score` INT DEFAULT NULL,
    `credit_source` VARCHAR(50) DEFAULT NULL,
    `education_level` VARCHAR(50) DEFAULT NULL,
    `verify_status` ENUM('pending', 'approved', 'rejected') NOT NULL DEFAULT 'pending',
    `reject_reason` VARCHAR(500) DEFAULT NULL,
    `verified_at` DATETIME DEFAULT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户实名认证表';

-- 1.3 角色表
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `role_code` VARCHAR(50) NOT NULL,
    `role_name` VARCHAR(100) NOT NULL,
    `description` VARCHAR(500) DEFAULT NULL,
    `status` ENUM('active', 'disabled') NOT NULL DEFAULT 'active',
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_role_code` (`role_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='角色表';

-- 1.4 权限表
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `permission_code` VARCHAR(100) NOT NULL,
    `permission_name` VARCHAR(100) NOT NULL,
    `module` VARCHAR(50) NOT NULL,
    `description` VARCHAR(500) DEFAULT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_permission_code` (`permission_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='权限表';

-- 1.5 用户角色关联表
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT UNSIGNED NOT NULL,
    `role_id` BIGINT UNSIGNED NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_user_role` (`user_id`, `role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户角色关联表';

-- 1.6 角色权限关联表
DROP TABLE IF EXISTS `role_permission`;
CREATE TABLE `role_permission` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `role_id` BIGINT UNSIGNED NOT NULL,
    `permission_id` BIGINT UNSIGNED NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_role_permission` (`role_id`, `permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='角色权限关联表';

-- 1.7 审计日志表
DROP TABLE IF EXISTS `audit_log`;
CREATE TABLE `audit_log` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `user_id` INT DEFAULT NULL COMMENT '操作用户ID',
    `username` VARCHAR(50) DEFAULT NULL COMMENT '用户名',
    `module` VARCHAR(50) DEFAULT NULL COMMENT '操作模块',
    `action` VARCHAR(100) DEFAULT NULL COMMENT '操作事项',
    `method` VARCHAR(10) DEFAULT NULL COMMENT '请求方法',
    `path` VARCHAR(200) DEFAULT NULL COMMENT '请求路径',
    `ip` VARCHAR(50) DEFAULT NULL COMMENT '请求IP',
    `user_agent` VARCHAR(500) DEFAULT NULL,
    `request_body` TEXT DEFAULT NULL,
    `response_code` INT DEFAULT NULL,
    `duration_ms` INT DEFAULT NULL COMMENT '耗时ms',
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `idx_user_id` (`user_id`),
    KEY `idx_module` (`module`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='审计日志表';

-- ============================================================
-- 初始化数据
-- ============================================================

-- 初始化角色
INSERT INTO `role` (`role_code`, `role_name`, `description`) VALUES
('ROLE_NORMAL_USER', '普通用户', '购房者'),
('ROLE_VERIFIED_USER', '实名用户', '已完成实名认证'),
('ROLE_DEVELOPER', '开发商', '房产开发企业'),
('ROLE_OPERATOR', '运营人员', '平台运营'),
('ROLE_ADMIN', '管理员', '系统管理员');

-- 初始化管理员账号 (密码: 123456)
INSERT INTO `user` (`phone`, `username`, `password_hash`, `nickname`, `user_level`, `status`) VALUES
('13888888888', 'admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.G8yHMlPKC.KCRW', '超级管理员', 'verified', 'active');

-- 给管理员分配角色
INSERT INTO `user_role` (`user_id`, `role_id`) VALUES (1, 5);
