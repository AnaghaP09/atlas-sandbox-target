// Package netaddr formats network addresses for test helpers.
package netaddr

import "strconv"

// JoinHostPort combines a host and a port into a "host:port" address.
func JoinHostPort(host string, port int) string {
	return host + ":" + strconv.Itoa(port)
}
