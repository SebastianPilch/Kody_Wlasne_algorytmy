`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.06.2023 14:12:22
// Design Name: 
// Module Name: procek
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


module procek(

    );
    reg clk=1'b0;
    initial
    begin
        while(1)
        begin
            #1 clk=1'b0;
            #1 clk=1'b1;
        end
    end
    
    reg[7:0] gpi = 8'd0;
    wire[7:0] gpo ;
    initial begin
    gpi = 1;
    #1000000;// sekunda
    /// opoünienie sygna≥u do zapalenia diody 2
    #400;
    gpi = 2;
    // 
    #1000000; // sekunda
    /// opoünienie sygna≥u do zapalenia zapÍtlenia
    #300;
    gpi = 1;
    
    
    #1000000000;// sekunda
    /// opoünienie sygna≥u do zapalenia diody 2
    #200;
    gpi = 2;
    // 
    #1000000; // sekunda
    /// opoünienie sygna≥u do zapalenia zapÍtlenia
    #100;
    gpi = 1;
    
    end
    procesor procek_ (
    .clk(clk),
    .gpi(gpi),
    .gpo(gpo)
    );
    
endmodule
