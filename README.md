# ESP32 Deep Sleep Test

```python
import machine
machine.deepsleep(sec*1000)
```

- Idle (after WiFi connection) : 40~60 mA
- Deep Sleep : 5 mA
- Establish WiFi Connection : 100~150mA, 1.5s
