
# Install
## Sensor PI
1. Install Hypriot
2. Docker portainer
<code>
  </code>
3. Docker grafana
<code>
  docker run \
  -d \
  -p 3000:3000 \
  --name=grafana \
  -v /home/pirate/grafana:/var/lib/grafana \
  fg2it/grafana-armhf:v4.1.2
</code>
  
