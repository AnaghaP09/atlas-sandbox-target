package netaddr

import "testing"

// Behavioural check written before any task exists. It must fail on the original code and pass
// after a correct fix. Changes to this directory are outside every task's permitted scope.

func TestJoinHostPortIPv6(t *testing.T) {
	cases := []struct {
		host string
		port int
		want string
	}{
		{"::1", 8080, "[::1]:8080"},
		{"fd00::10", 443, "[fd00::10]:443"},
		{"fe80::1%eth0", 80, "[fe80::1%eth0]:80"},
	}
	for _, c := range cases {
		if got := JoinHostPort(c.host, c.port); got != c.want {
			t.Errorf("JoinHostPort(%q, %d) = %q, want %q", c.host, c.port, got, c.want)
		}
	}
}

func TestJoinHostPortIPv4Unchanged(t *testing.T) {
	if got := JoinHostPort("192.0.2.1", 22); got != "192.0.2.1:22" {
		t.Errorf("IPv4 formatting changed: got %q", got)
	}
	if got := JoinHostPort("example.test", 80); got != "example.test:80" {
		t.Errorf("hostname formatting changed: got %q", got)
	}
}
