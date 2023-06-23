`timescale 1ns / 1ps
//-----------------------------------------------
// Company: agh
//-----------------------------------------------
module d_mem
(
  input [7:0]address,
  output [7:0]data
);
//-----------------------------------------------
//data memory
wire [7:0]data_memory[255:0];
assign data_memory[0]=8'd198;  /// wartoœæ 256 - i do liczenia 1sek do R0
assign data_memory[1]=8'd171; /// wartoœæ 256 - j do liczenia 1sek do R1
assign data_memory[2]=8'd207; /// wartoœæ 256 - k do liczenia 1sek do R2
  
//-----------------------------------------------
assign data=data_memory[address];
//-----------------------------------------------
endmodule
//-----------------------------------------------