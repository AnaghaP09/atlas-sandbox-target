// Package netaddr formats network addresses for test helpers.
package netaddr

import (
	"strconv"
	"strings"
)

// JoinHostPort combines a host and a port into a "host:port" address.
func JoinHostPort(host string, port int) string {
	if strings.Contains(host, ":") && !(strings.HasPrefix(host, "[") && strings.HasSuffix(host, "]")) {
		host = "[" + host + "]"
	}
	return host + ":" + strconv.Itoa(port)
}
