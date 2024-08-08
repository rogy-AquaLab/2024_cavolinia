#include <chrono>
#include <functional>
#include <rclcpp/rclcpp.hpp>
#include <string>
#include "trapezoidal_acc/trapezoid.hpp"

Trapezoid::Trapezoid(): 
    rclcpp::Node("trapezoid_acc"),
    current_velocity(0.0), //現在の速度（初期化）
    target_velocity(10.0)// 目標速度
{
    trapezoid_publisher = this->create_publisher<power_map_msg::msg::NormalizedPower>("/app/unsafe_power", 10);
    trapezoid_subscription = this->create_subscription<power_map_msg::msg::NormalizedPower>(
        "safe_power", 10, std::bind(&Trapezoid::trapezoid_topic_callback, this, std::placeholders::_1));

    timer = this->create_wall_timer(
        std::chrono::milliseconds(100), std::bind(&Trapezoid::_loop, this));
}

void Trapezoid::trapezoid_topic_callback(const power_map_msg::msg::NormalizedPower& msg)
{
    RCLCPP_DEBUG(this->get_logger(), "Received trapezoid_message");
    normalized_power= msg;
}

void Trapezoid::_loop() //速度のアルゴリズムがあまり理解できていないです。。
{
    double threshold_velocity = 5.0; // 速度の限度（仮に5.0とする。）

  // 速度がしきい値を超えた場合に速度を変更
    if (current_velocity > threshold_velocity) 
    {
        current_velocity = threshold_velocity;
    } 

    auto message = power_map_msg::msg::NormalizedPower();
    trapezoid_publisher->publish(message);
}