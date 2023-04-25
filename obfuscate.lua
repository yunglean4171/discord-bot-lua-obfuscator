local thing = [[
--SCRIPT
]]

local jcm="\n\n --// Obfuscated with nObf by Nertigel \n\n"
local jcfs={"ilInErTiGElilI","ilINertIgeL5391nErt","IlinErTiGeLilI","iElIinlTI5391ilI","nErtIgElwAshErE","nE5rtIgElwAshErE","nErtIgEl5391E","nE5391rtIgEl5391E"}
local jcq="local "..jcfs[math.random(1,#jcfs)].." = (5*3-2/8+9*2/9+8*3)".." "
local jcn1="function nErTiGeL_ilIilI("..jcfs[math.random(1,#jcfs)]..")"..jcq.."end".." "
local jcn2="function nErtIgEL_ilIilI("..jcfs[math.random(1,#jcfs)]..")"..jcq.."end".." "
local junkcode=jcm..jcn1..jcn2..jcq

local encoded = thing:gsub(".", function(bb) return "\\" .. bb:byte() end) or thing .. "\""

print(jcm..jcn1..jcq..'load("'..encoded..'")() '..jcq..jcn2..jcq)
