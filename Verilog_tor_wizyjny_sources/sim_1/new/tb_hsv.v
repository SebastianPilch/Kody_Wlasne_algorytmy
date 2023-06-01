`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 17.05.2023 21:27:33
// Design Name: 
// Module Name: tb_hsv
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


module tb_hsv(

    );
wire rx_pclk;

wire rx_de;
wire rx_hsync;
wire rx_vsync;

wire [7:0] rx_red;
wire [7:0] rx_green;
wire [7:0] rx_blue;


wire tx_de;
wire tx_hsync;
wire tx_vsync;

wire [7:0] tx_red;
wire [7:0] tx_green;
wire [7:0] tx_blue;



// --------------------------------------
// HDMI input
// --------------------------------------
hdmi_in64 file_input (
    .hdmi_clk(rx_pclk), 
    .hdmi_de(rx_de), 
    .hdmi_hs(rx_hsync), 
    .hdmi_vs(rx_vsync), 
    .hdmi_r(rx_red), 
    .hdmi_g(rx_green), 
    .hdmi_b(rx_blue)
    );
	 

wire lut_de;
wire lut_hsync;
wire lut_vsync;

wire [7:0] lut_red;
wire [7:0] lut_green;
wire [7:0] lut_blue;
wire [2:0] sw;

wire bin_de;
wire bin_hsync;
wire bin_vsync;
wire [7:0] bin_red;
wire [7:0] bin_green;
wire [7:0] bin_blue;


rgb2hsv vp_i (
//rgb2ycbcr_0 vp_i (
    .clk(rx_pclk),
    .de_in(rx_de),
    .h_sync_in(rx_hsync),
    .v_sync_in(rx_vsync),
    .pixel_in({rx_red,rx_green,rx_blue}),
    
    .de_out(lut_de),
    .h_sync_out(lut_hsync),
    .v_sync_out(lut_vsync),
    .pixel_out({lut_red,lut_green,lut_blue})
);
	 
// --------------------------------------
// Output assigment
// --------------------------------------
assign tx_de = rx_de;
assign tx_hsync = rx_hsync;
assign tx_vsync = rx_vsync;
assign tx_red = rx_red;
assign tx_green = rx_green;
assign tx_blue = rx_blue;

// --------------------------------------
// HDMI output
// --------------------------------------
hdmi_out64 file_output (
    .hdmi_clk(rx_pclk), 
    .hdmi_vs(lut_vsync), 
    .hdmi_de(lut_de), 
    .hdmi_data({8'b0,{lut_red,lut_green,lut_blue}})
    );


endmodule
