#!/bin/sh
### BEGIN INIT INFO
# Provides:          servoblaster
# Required-Start:    hostname $local_fs
# Required-Stop:
# Should-Start:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop servod
# Description:       This script starts/stops servod.
### END INIT INFO

PATH=/sbin:/usr/sbin:/bin:/usr/bin
. /lib/init/vars.sh

do_start () {
	sudo /usr/local/sbin/servod --idle-timeout=2000 --p1pins=16,18 >/tmp/out
    chmod a+rw /dev/i2c* > /dev/null 2>&1
	sleep 2
	python3 /usr/local/sbin/ptneutral.py 2>&1 &
}

do_status () {
	if [ -e /dev/servoblaster ] ; then
		return 0
	else
		return 4
	fi
}

case "$1" in
  start|"")
	do_start
	;;
  restart|reload|force-reload)
	killall servod
    do_start
	exit 3
	;;
  stop)
	killall servod
	;;
  status)
	do_status
	exit $?
	;;
  *)
	echo "Usage: servoblaster [start|stop|status]" >&2
	exit 3
	;;
esac

:
