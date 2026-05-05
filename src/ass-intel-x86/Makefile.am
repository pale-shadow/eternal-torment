# Use the cross-compiler tools
AS = aarch64-linux-gnu-as
LD = aarch64-linux-gnu-ld
GDB = gdb-multiarch

SRC = funk.s
OBJ = funk.o
EXEC = funk

# Define assembly flags, including debug options
# --gstabs includes stabs debugging symbols, compatible with GDB
ASFLAGS = --gstabs

.PHONY: all clean debug

all: $(EXEC)

$(EXEC): $(OBJ)
	$(LD) $(OBJ) -o $(EXEC)

$(OBJ): $(SRC)
	$(AS) $(ASFLAGS) $< -o $@

clean:
	rm -f $(OBJ) $(EXEC)

debug: all
	$(GDB) $(EXEC)
