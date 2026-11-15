package netaddr

import "testing"

func TestJoinHostPortIPv4(t *testing.T) {
	cases := map[string]struct {
		host string
		port int
		want string
	}{
		"loopback": {"127.0.0.1", 8080, "127.0.0.1:8080"},
		"address":  {"10.0.0.7", 443, "10.0.0.7:443"},
		"hostname": {"node-1.cluster.local", 6443, "node-1.cluster.local:6443"},
	}
	for name, c := range cases {
		if got := JoinHostPort(c.host, c.port); got != c.want {
			t.Errorf("%s: JoinHostPort(%q, %d) = %q, want %q", name, c.host, c.port, got, c.want)
		}
	}
}
