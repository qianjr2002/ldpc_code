import numpy as np
import matplotlib.pyplot as plt

# 自适应算法：根据 SNR 动态调整编码参数


def adaptive_ldpc_parameters(snr_db):
    """根据 SNR 动态选择 LDPC 参数"""
    if snr_db < 0:
        return {"rate": 0.5, "code_length": 128}  # 低码率
    elif 0 <= snr_db < 10:
        return {"rate": 0.75, "code_length": 256}  # 中等码率
    else:
        return {"rate": 0.9, "code_length": 512}  # 高码率

# 模拟 LDPC 性能


def simulate_ldpc_performance(snr_db_range):
    ber_results = []
    throughput_results = []

    for snr_db in snr_db_range:
        # 获取动态调整的参数
        params = adaptive_ldpc_parameters(snr_db)
        rate = params["rate"]
        code_length = params["code_length"]

        # 模拟 BER：示例公式，可替换为实际 LDPC 编码仿真
        snr_linear = 10 ** (snr_db / 10)
        ber = 0.5 / (1 + snr_linear * rate)  # 假设公式

        # 计算吞吐量
        throughput = rate * (1 - ber)

        # 存储结果
        ber_results.append(ber)
        throughput_results.append(throughput)

    return ber_results, throughput_results


# 绘制 BER 和吞吐量曲线在同一个窗口中
def plot_results(snr_db_range, ber_results, throughput_results):
    # 创建子图
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    # 绘制 BER 曲线
    axes[0].semilogy(snr_db_range, ber_results, label="BER", linestyle="--")
    axes[0].set_title("BER Performance with Adaptive LDPC Coding")
    axes[0].set_xlabel("SNR (dB)")
    axes[0].set_ylabel("BER (log scale)")
    axes[0].grid(True, which="both")
    axes[0].legend()

    # 绘制吞吐量曲线
    axes[1].plot(snr_db_range, throughput_results,
                 label="Throughput", linestyle="-")
    axes[1].set_title("Throughput with Adaptive LDPC Coding")
    axes[1].set_xlabel("SNR (dB)")
    axes[1].set_ylabel("Throughput")
    axes[1].grid(True, which="both")
    axes[1].legend()

    # 调整布局
    plt.tight_layout()
    plt.show()


def main():
    # 设置信噪比范围
    snr_db_range = np.arange(-5, 20, 1)
    # 仿真性能
    ber_results, throughput_results = simulate_ldpc_performance(snr_db_range)
    plot_results(snr_db_range, ber_results, throughput_results)


if __name__ == "__main__":
    main()
