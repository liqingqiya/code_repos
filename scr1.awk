#!/usr/bin/awk -f
/^$/{print "this is a blank line"}
{print $2, $1}
