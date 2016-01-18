#!/bin/bash
SESSION=$USER

tmux -2 new-session -d -s $SESSION

tmux split-window -h
tmux select-pane -t 0

tmux send-keys "hostapd hostapd.conf" C-m

sleep 10

tmux select-pane -t 1

tmux send-keys "ifconfig wlan0 10.20.0.1/24 up" C-m

sleep 1

tmux send-keys "dnsmasq -d -C dnsmasq.conf" C-m

tmux split-window -v

tmux send-keys "./firewall.sh" C-m
tmux send-keys "python server.py" C-m 

