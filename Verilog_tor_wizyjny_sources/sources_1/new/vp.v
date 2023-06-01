`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 30.03.2023 11:28:34
// Design Name: 
// Module Name: vp
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


module vp(
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
    
    wire[7:0] out_bit_R;
    wire[7:0] out_bit_G;
    wire[7:0] out_bit_B;
    
    Lut_do_binaryzacji R_bit
    (
    .a(pixel_in[7:0]),
    .clk(clk),
    .qspo(out_bit_R)
    );
    
    Lut_do_binaryzacji G_bit
    (
    .a(pixel_in[15:8]),
    .clk(clk),
    .qspo(out_bit_G)
    );
    
    Lut_do_binaryzacji B_bit
    (
    .a(pixel_in[23:16]),
    .clk(clk),
    .qspo(out_bit_B)
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
    
//    assign pixel_out = pixel_in;
//    assign pixel_out = {24{out_bit_R & out_bit_G & out_bit_B}};
    assign pixel_out[7:0] = out_bit_R;
    assign pixel_out[15:8] = out_bit_G;
    assign pixel_out[23:16] = out_bit_B;
    
endmodule
