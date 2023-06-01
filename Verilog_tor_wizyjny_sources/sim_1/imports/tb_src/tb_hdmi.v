`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: AGH
// Engineer: Tomasz Kryjak
// 
// Create Date:    11:29:28 10/28/2013 
// Design Name: 
// Module Name:    tb_filter 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module tb_hdmi(
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
hdmi_in file_input (
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


vp_tor_bez_efektow vp_i (
//rgb2ycbcr_0 vp_i (
    .clk(rx_pclk),
    .de_in(rx_de),
    .h_sync_in(rx_hsync),
    .v_sync_in(rx_vsync),
    .pixel_in({rx_red,rx_green,rx_blue}),
//    .sw(sw),
    
    .de_out(lut_de),
    .h_sync_out(lut_hsync),
    .v_sync_out(lut_vsync),
    .pixel_out({lut_red,lut_green,lut_blue})
);
//bin_ycrcb czarnobiale
//(
//    .clk(rx_pclk),
//    .de_in(lut_de),
//    .v_sync_in(lut_vsync),
//    .h_sync_in(lut_hsync),
//    .pixel_in({lut_red,lut_green,lut_blue}),
//    .de_out(bin_de),
//    .v_sync_out(bin_vsync),
//    .h_sync_out(bin_hsync),
//    .pixel_out({bin_red,bin_green,bin_blue})
//);
    


	 
// --------------------------------------
// Output assigment
// --------------------------------------
assign tx_de = rx_de;
assign tx_hsync = rx_hsync;
assign tx_vsync = rx_vsync;
assign tx_red = rx_red;
assign tx_green = rx_green;
assign tx_blue = rx_blue;
	 
//assign tx_de = bin_de;
//assign tx_hsync = bin_hsync;
//assign tx_vsync = bin_vsync;
//assign tx_red = bin_red;
//assign tx_green = bin_green;
//assign tx_blue = bin_blue;	 

// --------------------------------------
// HDMI output
// --------------------------------------
hdmi_out file_output (
    .hdmi_clk(rx_pclk), 
    .hdmi_vs(tx_vsync), 
    .hdmi_de(tx_de), 
    .hdmi_data({8'b0,tx_red,tx_green,tx_blue})
    );


endmodule
