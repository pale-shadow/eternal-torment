# Define the resulting executable name 
bin_PROGRAMS = hello

hello_SOURCES = hello.s
hello_LDFLAGS = -nostartfiles

hello_LINK = $(CCLD) $(AM_CFLAGS) $(CFLAGS) $(AM_LDFLAGS) $(LDFLAGS) -o $@

AM_CCASFLAGS = $(ASFLAGS)
