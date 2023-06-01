`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 13.03.2023 14:05:18
// Design Name: 
// Module Name: FlipFlop
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


module FlipFlop #
   (
    parameter N = 12
    
   )
   (
    input[N-1:0] in_data,
    output[N-1:0] out_data,
    input clk
    );
    reg[N-1:0]in_data_reg;
    always @(posedge clk)
    begin
        in_data_reg <= in_data;
    end
    assign out_data = in_data_reg;  
endmodule

