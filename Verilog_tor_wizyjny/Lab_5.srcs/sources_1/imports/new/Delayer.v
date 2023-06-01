`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 13.03.2023 13:55:58
// Design Name: 
// Module Name: Delayer
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


module Delayer  #
   (
    parameter N = 8,
    parameter DELAY = 10
   )
   (
    input[N-1:0] in,
    output[N-1:0] out,
    input clk
    );
    wire[N-1:0]flipflop[DELAY:0];
    assign flipflop[0] = in;  
    genvar i; 
    generate
        for(i = 0;i < DELAY;i = i+1)
        begin
        FlipFlop 
        #
        (
        .N(N)
        )
        D_FF
        (
            .in_data(flipflop[i]),
            .out_data(flipflop[i+1]),
            .clk(clk)
        );
        end
    endgenerate
    assign out = flipflop[DELAY];
endmodule
