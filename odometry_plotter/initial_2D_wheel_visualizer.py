import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class OdomVisualizer(Node):
    def __init__(self):
        super().__init__('odom_visualizer')
        self.subscription = self.create_subscription(
            PoseStamped,
            '/initial_2D_wheel',
            self.odom_callback,
            10
        )
        self.x_data = []
        self.y_data = []

        # Initialize the plot
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'b-', label='Path')  # Blue line for the path
        self.current_point, = self.ax.plot([], [], 'ro', label='Current Position')  # Red dot for the current position
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_xlabel('X Position')
        self.ax.set_ylabel('Y Position')
        self.ax.set_title('Robot Trajectory')
        self.ax.legend()

        # Start animation
        self.ani = FuncAnimation(self.fig, self.update_plot, init_func=self.init_plot, blit=True)

    def odom_callback(self, msg):
        # Extract the robot's x and y position from the PoseStamped message
        x = msg.pose.position.x
        y = msg.pose.position.y

        # Store the position data
        self.x_data.append(x)
        self.y_data.append(y)

    def init_plot(self):
        # Initialize the plot with empty data
        self.line.set_data([], [])
        self.current_point.set_data([], [])
        return self.line, self.current_point

    def update_plot(self, frame):
        if self.x_data and self.y_data:  # Ensure there is data to plot
            # Update the line (path) and the current position
            self.line.set_data(self.x_data, self.y_data)
            self.current_point.set_data(self.x_data[-1], self.y_data[-1])  # Current position as a red dot
        return self.line, self.current_point


def main(args=None):
    rclpy.init(args=args)
    node = OdomVisualizer()
    plt.show(block=False)
    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.05)
            plt.pause(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        plt.close()
        # Cleanup and shutdown
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()