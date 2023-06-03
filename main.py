from jnius import autoclass

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
UUID = autoclass('java.util.UUID')

def get_socket_stream(name):
    paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
    socket = None
    for device in paired_devices:
        if device.getName() == name:
            socket = device.createRfcommSocketToServiceRecord(
                UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
            recv_stream = socket.getInputStream()
            send_stream = socket.getOutputStream()
            break
    socket.connect()
    return recv_stream, send_stream

if __name__ == '__main__':
    layout = '''
BoxLayout:
    orientation:"vertical"
    padding:50
    spacing:20
    Label:
        text: 'Kivy with Bluetooth'
    Button:
        id: b1
        text: '-A CLICK-'
        on_release: app.send(b'Hi_Kivy')
    Button:
        id: b2
        text: '-B CLICK-'
        on_release: app.send(b'get_B')
    Button:
        id: b3
        text: '-C CLICK-'
        on_release: app.send(b'get_C')
    '''
    from kivy.lang import Builder
    from kivy.app import App

    class Bluetooth(App):
        def build(self):
            self.recv_stream, self.send_stream = get_socket_stream('ESP32_BT')
            return Builder.load_string(layout)

        def send(self, message):
            self.send_stream.write(message)
            self.send_stream.flush()

    Bluetooth().run()