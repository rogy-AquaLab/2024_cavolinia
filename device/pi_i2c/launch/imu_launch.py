from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    imu = Node(
        package="pi_i2c",
        executable="imu",
        namespace="device",
    )
    return LaunchDescription([imu])
