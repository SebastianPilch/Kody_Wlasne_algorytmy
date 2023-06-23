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


module mux8_1(

    input[7:0] R0,
    input[7:0] R1,
    input[7:0] R2,
    input[7:0] R3,
    input[7:0] R4,
    input[7:0] R5,
    input[7:0] R6,
    input[7:0] R7,
    
    input[2:0] adres, 
    output[7:0] out
    );
    wire[7:0]out_reg[7:0]; 
    assign out_reg[0] = R0;
    assign out_reg[1] = R1;
    assign out_reg[2] = R2;
    assign out_reg[3] = R3;
    assign out_reg[4] = R4;
    assign out_reg[5] = R5;
    assign out_reg[6] = R6;
    assign out_reg[7] = R7;
    
    assign out = out_reg[adres];
endmodule
