`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 15.06.2023 14:37:15
// Design Name: 
// Module Name: warunek_skoku
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


module warunek_skoku(
    
    input[1:0] rodzaj_skoku,
    input zero_con,
    output skok
    
    );
    reg s=0;
    always @* begin
    // brak skoku
    if (rodzaj_skoku == 2'b00) begin
        s = 1'b0;
    end
    //bezwarunkowy
    if(rodzaj_skoku == 2'b01) begin
        s =1'b1;
    end
    // warunkowy jz jump if zero 10  
    if(rodzaj_skoku==2'b10) begin
        s = ((zero_con) ? 1'b0:1'b1);
    end
    if(rodzaj_skoku==2'b11)begin
        s = ((zero_con) ? 1'b0:1'b1);
    end
    end
    assign skok = s;
    
    
endmodule
