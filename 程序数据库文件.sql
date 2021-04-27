/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80021
Source Host           : localhost:3306
Source Database       : liberary

Target Server Type    : MYSQL
Target Server Version : 80021
File Encoding         : 65001

Date: 2021-04-27 17:44:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` double(10,2) NOT NULL,
  `publisher` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES ('1', 'Go语言高并发与微服务实战', '85.40', '中国铁道出版社');
INSERT INTO `book` VALUES ('2', '汇编语言（第4版）', '39.80', '芝麻开门图书专营店');
INSERT INTO `book` VALUES ('3', '\'Python\', \'三剑客：Python\', \'从入门到实践第2版+快速上手第2版+极客\', \'（套装共3册）\'', '165.50', '人民邮电出版社');
INSERT INTO `book` VALUES ('4', 'Python从入门到精通 清华大学出版社', '24.00', '墨马图书旗舰店');
INSERT INTO `book` VALUES ('5', '深度学习入门', '29.50', '博库网旗舰店');
INSERT INTO `book` VALUES ('6', 'C++ Primer Plus 第6版 中文版', '59.00', '人民邮电出版社');
INSERT INTO `book` VALUES ('7', 'JavaScript高级程序设计 第4版(图灵出品）', '87.30', '人民邮电出版社');
INSERT INTO `book` VALUES ('8', 'python从入门到精通', '27.90', '广东人民出版社官方旗舰店');
INSERT INTO `book` VALUES ('9', 'java从入门到精通(第5版)', '28.80', '墨马图书旗舰店');
INSERT INTO `book` VALUES ('10', 'Java核心技术系列', '638.00', '芝麻开门图书专营店');
