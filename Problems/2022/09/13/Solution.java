class Solution {
    public boolean validUtf8(int[] data) {
        int[][] bytes = new int[data.length][8];
        for (int i = 0; i < data.length; i++) {
            bytes[i] = toBinary(data[i]);
        }
        return helper(bytes, 0);
    }

    private boolean helper(int[][] data, int i) {
        if (i == data.length) {return true;}
        if (isOneByte(data, i) && helper(data, i+1)) {return true;}
        if (isTwoByte(data, i) && helper(data, i+2)) {return true;}
        if (isThreeByte(data, i) && helper(data, i+3)) {return true;}
        if (isFourByte(data, i) && helper(data, i+4)) {return true;}
        return false;
    }

    private boolean isOneByte(int[][] data, int i) {
        return data[i][0] == 0;
    }

    private boolean isTwoByte(int[][] data, int i) {
        if (data[i][0] == 0 || data[i][1] == 0 || data[i][2] == 1) {return false;}
        if (i+1 == data.length) {return false;}
        return data[i+1][0] == 1 && data[i+1][1] == 0;
    }

    private boolean isThreeByte(int[][] data, int i) {
        if (data[i][0] == 0 || data[i][1] == 0 || data[i][2] == 0 || data[i][3] == 1) {return false;}
        if (i+2 >= data.length) {return false;}
        return data[i+1][0] == 1 && data[i+1][1] == 0 && data[i+2][0] == 1 && data[i+2][1] == 0;
    }

    private boolean isFourByte(int[][] data, int i) {
        if (data[i][0] == 0 || data[i][1] == 0 || data[i][2] == 0 || data[i][3] == 0 || data[i][4] == 1) {return false;}
        if (i+3 >= data.length) {return false;}
        return data[i+1][0] == 1 && data[i+1][1] == 0 && data[i+2][0] == 1 && data[i+2][1] == 0 && data[i+3][0] == 1 && data[i+3][1] == 0;
    }

    private int[] toBinary(int num) {
        int[] bin = new int[8];
        for (int i = 0; i < 8; i++) {
            if ((num & 1) > 0) {
                bin[7-i] = 1;
            }
            num >>= 1;
        }
        return bin;
    }
}
