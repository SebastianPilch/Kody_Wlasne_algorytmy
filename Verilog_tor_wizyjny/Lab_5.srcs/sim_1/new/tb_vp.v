`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10.04.2023 21:55:49
// Design Name: 
// Module Name: tb_vp
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


module tb_vp(
    );
    
    reg clk = 1'b0;
    
    initial begin
        forever begin
        #1 clk = ~clk;
        end
    end
    
    wire v_s;
    wire h_s;
    wire d_o;
    wire[7:0] r;
    wire[7:0] g;
    wire[7:0] b;
    reg[7:0] red;
    reg[7:0] green;
    reg[7:0] blue;
    wire[23:0] out;
    integer i;
    integer j;
    integer k;
 initial begin
    for(i =0;i<255;i=i+1) begin
        #1
        red = i;  
        for(j =0;j<255;j=j+1) begin
            #1
            green = j;
            for(k =0;k<255;k=k+1) begin
                #1
                blue = k;
            end
        end
    end
 end
    
    vp_binaryzacja modul_test(
    .clk(clk),
    .de_in(1'b0),
    .v_sync_in(1'b0),
    .h_sync_in(1'b0),
    .pixel_in({{red,green,blue}}),
    .de_out(d_o),
    .v_sync_out(v_s),
    .h_sync_out(h_s),
    .pixel_out(out),
    .pixel_r(r),
    .pixel_g(g),
    .pixel_b(b)
    
    


    );
endmodule
