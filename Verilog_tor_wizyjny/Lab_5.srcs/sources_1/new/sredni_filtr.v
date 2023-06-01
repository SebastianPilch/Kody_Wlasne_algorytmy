`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 30.05.2023 18:52:56
// Design Name: 
// Module Name: sredni_filtr
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


module sredni_filtr
#(
    parameter H_SIZE = 83
//    parameter IMG_W = 64,
//    parameter IMG_H = 64
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
    
    reg rst=0;
    reg ce = 1;
    reg[10:0]D11;
    reg[10:0]D12;
    reg[10:0]D13;
    
    reg[10:0]D21;
    reg[10:0]D22;
    reg[10:0]D23;

    reg[10:0]D31;
    reg[10:0]D32;
    reg[10:0]D33;
  
    reg[12:0] sumRow1 = 0;
    reg[12:0] sumRow2 = 0;
    reg[12:0] sumRow3 = 0;
    reg[14:0] sumAll = 0;
    wire context_valid;
    wire flag_v;
    wire flag_h;
    reg[23:0] new_color;

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
            
        
        sumRow1 = {4'b0,D11[10:3]} + {3'b0,D12[10:3],1'b0} + {4'b0,D13[10:3]};
        sumRow2 = {3'b0,D21[10:3],1'b0} + {2'b0,D22[10:3],2'b0} + {3'b0,D23[10:3],1'b0};
        sumRow3 = {4'b0,D31[10:3]} + {3'b0,D32[10:3],1'b0} + {4'b0,D33[10:3]};
        sumAll = sumRow1 + sumRow2 + sumRow3;
        new_color = (sumAll[14:4] > 11'd255) ? 24'hffffff : {3{sumAll[11:4]}};
    end

    delayLineBRAM_long_WP
    #
    (
     .WIDTH(22)
    ) 
    Wp_srednie(
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
    .DELAY(2)
    )
     del_
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
