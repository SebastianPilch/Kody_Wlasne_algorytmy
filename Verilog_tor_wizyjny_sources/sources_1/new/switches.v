`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 13.04.2023 11:34:15
// Design Name: 
// Module Name: switches
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


module switches(
    input[1:0] sw,
    output[1:0] adres
    
    );
    assign adres[0] = sw[0];
    assign adres[1] = sw[1];
endmodule
