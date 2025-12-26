import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
  
def generate_launch_description():
  
    server = launch_ros.actions.Node(
        package='mypkg',      #パッケージの名前を指定
        executable='server',  #実行するファイルの指定
        )
    client = launch_ros.actions.Node(
        package='mypkg',
        executable='client',
        output='screen',        #ログを端末に出すための設定
        arguments=['successful_pass737300'],
        )
 
    return launch.LaunchDescription([server, client])   
