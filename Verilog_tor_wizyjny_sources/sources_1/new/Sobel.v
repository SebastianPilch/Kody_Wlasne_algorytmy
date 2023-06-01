`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 31.05.2023 19:01:51
// Design Name: 
// Module Name: Sobel
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


module Sobel
    #(
        parameter H_SIZE = 83
    )
    (
        input clk,
    input de,
    input vsync,
    input hsync,
    input[23:0] pixel_in,
    
    output de_out,
    output v_sync_out,
    output h_sync_out,
    output[23:0] pixel_out
    
    );
    
    reg[10:0] data;
    wire[21:0] WP_out;
    
    
    reg[10:0]D11;
    reg[10:0]D12;
    reg[10:0]D13;
    
    reg[10:0]D21;
    reg[10:0]D22;
    reg[10:0]D23;

    reg[10:0]D31;
    reg[10:0]D32;
    reg[10:0]D33;
    
    reg signed[14:0] sumRow1 = 0;
    reg signed[14:0] sumRow3 = 0;
    reg signed[14:0] Sx = 0;
    reg signed[14:0] AbsSx = 0;
    reg signed[14:0] sumCol1 = 0;
    reg signed[14:0] sumCol3 = 0;
    reg signed[14:0] Sy = 0;   
    reg signed[14:0] AbsSy = 0;
    reg signed[14:0] sumAll;
    reg[23:0] new_color;
    reg rst=0;
    reg ce = 1;
    always @(posedge clk)
    begin
        data <= {pixel_in[23:16],de,hsync,vsync};
        D11 <= data;
        D12 <= D11;
        D13 <= D12;
        
        D21 <= WP_out[21:11];
        D22 <= D21;
        D23 <= D22;

        D31 <= WP_out[10:0];
        D32 <= D31;
        D33 <= D32;
            
        
        sumRow1 = {4'b0,D31[10:3]} + {3'b0,D32[10:3],1'b0} + {4'b0,D33[10:3]};
        sumRow3 = {4'b0,D11[10:3]} + {3'b0,D12[10:3],1'b0} + {4'b0,D13[10:3]};
        Sx = sumRow1 - sumRow3;
        AbsSx = (Sx > 0) ? Sx : ~(Sx) + 1; 
        
        
        sumCol1 = {4'b0,D33[10:3]} + {3'b0,D23[10:3],1'b0} + {4'b0,D13[10:3]};
        sumCol3 = {4'b0,D31[10:3]} + {3'b0,D21[10:3],1'b0} + {4'b0,D11[10:3]};
        Sy = sumCol1 - sumCol3;
        AbsSy = (Sy > 0) ? Sy : ~(Sy) + 1; 
        sumAll = AbsSy + AbsSx;
        
        new_color = {3{sumAll[9:2]}};
        
    end
    
    
    delayLineBRAM_long_WP
    #
    (
     .WIDTH(22)
    ) 
    Wp_SX(
        .clk(clk),
        .rst(rst),
        .ce(ce),
        .h_size(H_SIZE-3),
        .din({D13,D23}),
        .dout(WP_out)
    );
    

        Delayer
    #(
    .N(3),
    .DELAY(1)
    )
     del
    (
    .clk(clk),
    .in(D22[2:0]),
    .out({context_valid,flag_h,flag_v})
    );
        
    assign pixel_out = new_color;
    assign v_sync_out = flag_v;
    assign h_sync_out = flag_h;
    assign de_out = context_valid;
    
    
endmodule
