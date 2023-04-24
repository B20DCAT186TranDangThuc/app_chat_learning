CREATE TABLE `Users` (
  `user_id` int primary key auto_increment,
  `username` varchar(255),
  `password` varchar(255),
  `fullname` varchar(255)
);

CREATE TABLE `Mesagers` (
  `message_id` int primary key auto_increment,
  `sender_id` int,
  `receiver_id` int,
  `message_content` varchar(255),
  `message_date` date
);

CREATE TABLE `ChatRooms` (
  `room_id` int primary KEY auto_increment,
  `user1_id` int,
  `user2_id` int,
  `message_id` int
);

ALTER TABLE `Mesagers` ADD FOREIGN KEY (`sender_id`) REFERENCES `Users` (`user_id`);
ALTER TABLE `Mesagers` ADD FOREIGN KEY (`receiver_id`) REFERENCES `Users` (`user_id`);
ALTER TABLE `ChatRooms` ADD FOREIGN KEY (`user1_id`) REFERENCES `Users` (`user_id`);
ALTER TABLE `ChatRooms` ADD FOREIGN KEY (`user2_id`) REFERENCES `Users` (`user_id`);
ALTER TABLE `ChatRooms` ADD FOREIGN KEY (`message_id`) REFERENCES `Mesagers` (`message_id`);
