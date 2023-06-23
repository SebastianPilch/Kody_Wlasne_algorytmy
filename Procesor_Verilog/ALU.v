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


module ALU(
    input[7:0] rx,
    input[7:0] ry,
    output[7:0] sum_out,
    output[7:0] and_out,
    output zero_con
);
    assign sum_out = rx + ry;
    assign and_out = rx & ry;
    assign zero_con = ((rx == 8'b00000000)? 1 : 0);
endmodule
