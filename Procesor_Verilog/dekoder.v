`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 15.06.2023 11:47:40
// Design Name: 
// Module Name: mux8_1
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module dekoder(
    input[2:0] address,
    output[7:0] out
);

assign out[0]=((address == 3'b000) ? 1'b1 : 1'b0);
assign out[1]=((address == 3'b001) ? 1'b1 : 1'b0);
assign out[2]=((address == 3'b010) ? 1'b1 : 1'b0);
assign out[3]=((address == 3'b011) ? 1'b1 : 1'b0);
assign out[4]=((address == 3'b100) ? 1'b1 : 1'b0);
assign out[5]=((address == 3'b101) ? 1'b1 : 1'b0);
assign out[6]=((address == 3'b110) ? 1'b1 : 1'b0);
assign out[7]=((address == 3'b111) ? 1'b1 : 1'b0);
endmodule
