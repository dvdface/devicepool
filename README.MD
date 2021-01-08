# feedback
* send email to dvdface@gmail.com
* visit https://github.com/dvdface/devicepool

# how to install
`pip install devicepool`

# how to use
1. import library first
`from devicepool import Device, DevicePool`
2. make a resource dict list
```
resource_list = [
	{
		'ip':	'192.168.1.1',
		'type': 'android'
	},
	
	{
		'ip':	'192.168.1.2',
		'type': 'ios'
	}
]
```
3. init devicepool
```
devicepool = DevicePool(resource_list)
```
4. get a device from the pool
```
# allocate any dev from resource pool
dev = devicepool.get()

# use filter_func to get desired resource, for exmaple type == 'android'
dev = devicepool.get(filter_func=lambda dev: dev.type == 'android')

# use tiimeout to wait, default timeout is zero
dev = devicepool.get(timeout=10)
```
5. check if allocating device is successfully
```
# if resource is not enougth and timeout, return None
# so you need check if dev is None
if dev == None:
	print('allocate resource failed')
```
6. use the device by dot way
```
print(dev.ip)
print(dev.type)
```
7. free the device, or let't it free automatically
```
del dev
```