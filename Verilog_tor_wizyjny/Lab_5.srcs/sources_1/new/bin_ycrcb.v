`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.04.2023 19:24:11
// Design Name: 
// Module Name: bin_ycrcb
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


module bin_ycrcb(
    input clk,
    input de_in,
    input v_sync_in,
    input h_sync_in,
    input[23:0] pixel_in,
    output de_out,
    output v_sync_out,
    output h_sync_out,
    output[23:0] pixel_out
    );
    
    wire[7:0] Cr;
    wire[7:0] Cb;
    
    Cr_bin Cr_bit
    (
    .a(pixel_in[7:0]),
    .clk(clk),
    .qspo(Cr)
    );
    
    bin_Cb Cb_bit
    (
    .a(pixel_in[15:8]),
    .clk(clk),
    .qspo(Cb)
    );
    

    reg r_de = 0;
    reg r_hsync = 0;
    reg r_vsync = 0;
    always @(posedge clk)
        begin
        r_de <= de_in;
        r_hsync <= h_sync_in;
        r_vsync <= v_sync_in;
    end
    assign de_out = r_de;
    assign h_sync_out = r_hsync;
    assign v_sync_out = r_vsync;
    
   assign pixel_out = {3{ Cr & Cb }};
    
endmodule
