# kivybluetooth
1.將藍牙與手機配對

2.在arduino中設定藍牙名稱
SerialBT.begin("ESP32_BT"); //藍牙顯示名稱，可自行更改，需避免與他人重複命名

3.在main.py更改藍牙名稱
self.recv_stream, self.send_stream = get_socket_stream('ESP32_BT')

4.在colab跑完後即可產生apk
